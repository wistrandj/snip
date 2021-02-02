snip_root=$(pwd)

function activate() {
    source ./env/bin/activate
}

function rx() {
    pip install "${snip_root}"
}
