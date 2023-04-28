class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            email_valid = local + '@' + domain
            emails_unique.add(email_valid)
        return len(emails_unique)