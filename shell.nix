{ nixpkgs ? import (fetchTarball https://github.com/NixOS/nixpkgs/archive/nixos-unstable.tar.gz) {} }:
with nixpkgs;

let
  customPython = python39.buildEnv.override {
    extraLibs = [
      python39Packages.black
      python39Packages.grpcio
      python39Packages.grpcio-tools
    ];
  };
in
  pkgs.mkShell {
    buildInputs = [
      customPython
      protobuf3_15
    ];
  }

