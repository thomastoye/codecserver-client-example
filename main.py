from codecserver.generated.handshake_pb2 import Handshake
from codecserver.generated.request_pb2 import Request
from codecserver.generated.check_pb2 import Check
from codecserver.generated.data_pb2 import ChannelData, SpeechData
from codecserver.generated.response_pb2 import Response

from google.protobuf.internal.decoder import _DecodeSignedVarint
from google.protobuf.internal.encoder import _EncodeSignedVarint

from google.protobuf.any_pb2 import Any

import wave
import asyncio

# codecserver location
HOST = "localhost"
PORT = 1073
# codecserver protocol version
PROTOCOL_VERSION = "0.2.0-dev"

# WAV file (8000Hz, 16-bit LE) for coding to AMBE
wr = wave.Wave_read('input.wav')

assert wr.getnchannels() == 1
assert wr.getframerate() == 8000
assert wr.getcomptype() == 'NONE'
assert wr.getsampwidth() == 2

# Create packets of 320 bytes each
packets = []

packet = wr.readframes(160)

while packet != b'':
    if len(packet) == 320:
        packets.append(packet)

    packet = wr.readframes(160)

print(f'number of WAV packets: {len(packets)}')

def decode_message(msg):
    line_break_pos = msg.index(b'\n')
    data_length = _DecodeSignedVarint(msg, 0)
    print(f'line break pos {line_break_pos} data length {data_length}')
    any_dec = Any()
    any_dec.ParseFromString(msg[line_break_pos : line_break_pos + data_length[0]])
    print(any_dec)

    if any_dec.type_url == "type.googleapis.com/CodecServer.proto.Handshake":
        handshake = Handshake()
        handshake.ParseFromString(any_dec.value)
        print(
            f"Got a handshake from the server. Server name: {handshake.serverName}, version {handshake.serverVersion}"
        )

        return handshake
    elif any_dec.type_url == "type.googleapis.com/CodecServer.proto.Response":
        response = Response()
        response.ParseFromString(any_dec.value)
        print(
            f"Got a response from the server. Status: {response.result}, message: {response.message}, framing hint: {response.framing}"
        )

        return response
    elif any_dec.type_url == 'type.googleapis.com/CodecServer.proto.SpeechData':
        speech_data = SpeechData()
        speech_data.ParseFromString(any_dec.value)
        print(
            f"Got speech data from the server. Data: {speech_data.data}"
        )

        return speech_data
    else:
        print(f"Unknown type_url: {any_dec.type_url}")

def encodeSignedVarInt(i):
    buf = bytes()

    def append_to_buf(e):
        nonlocal buf
        buf = buf + e

    _EncodeSignedVarint(value=i, write=append_to_buf)

    return buf

# Pack structure in an Any
def pack_for_sending(msg):
    any = Any()
    any.Pack(msg=msg)

    prefix = encodeSignedVarInt(any.ByteSize())

    return prefix + any.SerializeToString()



async def codec_server_client():
    reader, writer = await asyncio.open_connection(HOST, PORT)

    data = await reader.read(1024)
    decode_message(data)

    check = Check()
    check.codec = "ambe"

    print("send check")
    writer.write(pack_for_sending(check))
    await writer.drain()

    data = await reader.read(100)
    print("Received: %r" % data)
    decode_message(data)

    request = Request()
    request.settings.directions.append(request.settings.DECODE)
    request.settings.directions.append(request.settings.ENCODE)
    request.codec = "ambe"
    request.settings.args.update({"index": "33"})

    writer.write(pack_for_sending(request))
    await writer.drain()

    data = await reader.read(100)
    print("Received: %r" % data)
    decode_message(data)

    for wav_packet in packets:
        speech_data = SpeechData()
        speech_data.data = wav_packet

        writer.write(pack_for_sending(speech_data))
        await writer.drain()

        data = await reader.read(500)
        print("Received: %r" % data)
        decode_message(data)

    print("Close the connection")
    writer.close()
    await writer.wait_closed()


asyncio.run(codec_server_client())

