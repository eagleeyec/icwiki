# Matrix

## Setup synapse

      mkdir -p ~/synapse
      python3 -m venv venv
      source venv/bin/activate
      pip install --upgrade pip
      pip install --upgrade setuptools
      pip install matrix-synapse
      python -m synapse.app.homeserver     --server-name matrix.local     --config-path homeserver.yaml     --generate-config     --report-stats=no
      export LD_LIBRARY_PATH=/usr/local/lib
      synctl start
      register_new_matrix_user -c homeserver.yaml http://localhost:8008

https://upcloud.com/community/tutorials/install-matrix-synapse/