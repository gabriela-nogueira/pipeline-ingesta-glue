from scripts import scrapping, pre_processing, upload
import logging

def pipeline_extract_and_load():
    print("Starting the data extraction and upload pipeline to Amazon S3")

    try:
        print("⬇️ Downloading file...")

        scrapping.download_file()

        print("✅ Download completed successfully.")

        print("▶️ Starting initial pre-processing")

        pre_processing.pre_processed_data()

        print("✅ Final file created successfully.")

        print("▶️ Uploading data in Amazon S3.")

        upload.upload_data_to_s3()

        print("✅ Upload completed successfully.")

        
    except Exception as e:
        raise Exception(f"Unable to upload the file. {str(e)}")


if __name__ == "__main__":
    pipeline_extract_and_load()