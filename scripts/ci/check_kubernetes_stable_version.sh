#!/usr/bin/env bash

LATEST=$(curl -fsSL https://dl.k8s.io/release/stable.txt)
echo "k8s_latest=$LATEST"
echo "k8s_latest=$LATEST" >> $GITHUB_OUTPUT
echo "### Kubernetes version report" >> $GITHUB_STEP_SUMMARY
echo "- Latest stable release: ${{ steps.fetch_k8s.outputs.k8s_latest }}" >> $GITHUB_STEP_SUMMARY