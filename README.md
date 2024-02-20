

GPJ to MDB Converter and Data Pusher

This project aims to automate the process of finding, copying, and converting .gpj files in a server directory to .mdb format, which is readable by Microsoft Access. The ultimate goal is to extract the data from these files and push it to a MongoDB database.

Project Objectives
Find and Copy .gpj Files: The first step of the process is to locate all .gpj files within a specified server directory. These files are then copied to a designated folder for further processing.

Convert .gpj to .mdb: Once the .gpj files are secured, they are converted to .mdb format. This conversion is necessary because the data within the .gpj files needs to be read using Microsoft Access.

Read Data with Microsoft Access: With the files in .mdb format, Microsoft Access can be used to read and interpret the data. This step is crucial for understanding the structure and content of the data before it is pushed to MongoDB.

Push Data to MongoDB: The final step is to push the data to MongoDB. This involves establishing a connection to a MongoDB database and transferring the data from the .mdb files into the database.

This project is designed to streamline the process of data extraction and transfer, making it easier to manage and analyze the data stored in .gpj files. By automating this process, we can save time and reduce the risk of errors that can occur when these tasks are performed manually.