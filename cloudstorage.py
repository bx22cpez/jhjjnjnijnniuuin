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
    access_token = 'sl.BSB0OPly0N658KWGqQVi8-ZhOXZGIY0A5mlY013UJa5wObAZYwEGZLNiIWBIuBseOMnfN4RRQnMnba1XQL4zy1Er4a9-LiebjDard2U0TzXGezuFkVSP54zJb1B_jwGHSzdf2Tc'
    transferData = TransferData(access_token)

    file_from = 'C:/MyStory/Characters.txt'
    file_to = '/pics/Characters.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file is being uploaded")
    
if __name__ == '__main__':
    main()