ssh-keygen -t ed25519 -C"..."
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

git clone ...
cd ... (адрес папки)
