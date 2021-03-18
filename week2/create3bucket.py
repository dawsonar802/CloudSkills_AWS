import sys
import boto3


def main():
    creates3bucket(name)

def creates3bucket(name):
    client = boto3.client('s3')

    create = client.create_bucket(
        Bucket=name,
        ACL='private',
    )

    print(create)

name = sys.argv[1]

if __name__ == '__main__':
    main()
