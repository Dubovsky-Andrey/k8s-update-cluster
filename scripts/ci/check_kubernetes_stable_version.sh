          LATEST=$(curl -fsSL https://dl.k8s.io/release/stable.txt)
          echo "k8s_latest=$LATEST"
          echo "k8s_latest=$LATEST" >> $GITHUB_OUTPUT