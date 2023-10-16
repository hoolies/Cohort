#!/bin/bash
sudo ip link add name pbridge type bridge
sudo ip link add name ybridge type bridge
sudo ip link add name wbridge type bridge
sudo ip link add name obridge type bridge
brctl show
