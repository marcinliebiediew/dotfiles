function hash
echo -n "$argv" | openssl dgst -sha256
end
