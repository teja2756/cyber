# Secure Configuration Notes

## FTPS
- Prefer explicit TLS with certificate validation.
- Use strong account credentials stored outside source control.
- Restrict the transfer account's permissions.
- Disable plaintext FTP where possible.
- Validate server certificates.

## Steganography
Steganography should be treated as an additional concealment layer, not as a replacement for encryption.

For an authorized lab, tools such as steghide can be evaluated with non-sensitive test files.

## Malware scanning
If using an external scanning service such as VirusTotal:
- Never upload confidential files without authorization.
- Keep API keys in environment variables or a secrets manager.
- Review the service's privacy and upload policies.

## Key management
Never publish RSA private keys. Use `.gitignore` and a secure secret store.
