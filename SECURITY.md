## 🇬🇧 Security Policy
I take security and responsible handling of this project seriously.
Please **do not report security issues publicly** via Issues or Pull Requests.

### How to report a security issue
If you discover a vulnerability, security‑relevant behavior, or risk related to DNS / frAIme, please contact me directly:

**[schltdns@gmail.com]**

Provide as much detail as possible so I can reproduce and assess the issue.

### Response process
1. I will acknowledge your report as quickly as possible.
2. I will investigate the issue and provide an assessment.
3. I will keep you informed about status and planned actions.
4. I will only publish security‑related fixes once the risk is resolved.

Thank you for helping keep this project secure.

---

## Supported versions
| Version | Supported          |
|---------|--------------------|
| 2.1.x   | :white_check_mark: |
| 2.0.x   | :x:                |
| < 2.0   | :x:                |

## Security design principles (DNS / frAIme)
- **Input validation**: all model outputs are checked against thresholds before logging.
- **Auditability**: hash-chaining (P8) ensures log integrity; manipulation is detectable.
- **No persistent user data**: the reference implementation stores no personal data.
- **Multi-agent triangulation**: reduces single-model manipulation risk.
