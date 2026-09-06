// 0 ms | 19.2 MB
class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique_emails.add(f"{local}@{domain}")

        return len(unique_emails)