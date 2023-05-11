import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BeKW5MEKHpXmCxx3ulBt-I8tcG8JMxN_0F6ci5G57NrCIIyGqq-OW-ShBxCqAUb5emHY94xfljNV8BUPwVW6Y4sPA24JDnIiezK4Z-jl8oxS5KMUh1-m--YaZdjGm5AAvzriYBU'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()