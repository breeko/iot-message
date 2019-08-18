# iot-message

iot-message is a tool to monitor mqtt messages sent by AWS and use them to trigger arbitrary commands on an internet enabled device.

One use case can be to monitor github commits, initialize pull and restart a service.

## Setup MQTT

1. [Creata an iot thing on aws](https://docs.aws.amazon.com/iot/latest/developerguide/iot-plant-step2.html)

2. Place `root.ca.pem`, `xxx.cert.pem`, `xxx.private.key` in to certificates directory

3. Rename `config-example.yml` to `config.yml` and replace values for `certificatePath` and `privateKeyPath` with the names of the files from step 2. 

4. Update the arn of the iot device to `config.yml`. The arn should be prefixed with `arn` and can be found under details in the iot dashboard (e.g. `arn:aws:iot:us-east-1:xxx`)

5. Update the host of the iot device to `config.yml`. It can be found when you select thing from aws iot console (Manage -> Things -> [thing] -> Interact) and should look like a url (e.g. `xxx.iot.us-east-1.amazonaws.com`)

6. Set subsciptions and corresponding functions in `subscriptions.py`. By default if a subscription for the topic `topic` causes the console to print the message

7. From the src folder, run `python app.py`

## Testing messages

Messages can be sent from the aws iot console (Test -> Publish). Test by sending a message with the topic `topic`

## Sending messages via AWS Lambda

1. Go into the lambda directory and run `serverless deploy`

2. Based on the output, you should see a POST under endpoints with the url (e.g. `POST - https://xxx.amazonaws.com/dev/iotMessage/post`). You can test the endpoing using 

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"topic":"topic","message":"Hello from Lambda"}' \
  https://xxx.amazonaws.com/dev/iotMessage/post
```

 and you should see "Hello from Lambda" on your app console.



On device:

ssh-keygen -t rsa (enter for all defaults)
chmod 400 ~/.ssh/id_rsa.pub
nano ~/.ssh/config

```
Host [private-repo-name]
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa.pub
  IdentitiesOnly yes
```
chmod 400 ~/.ssh/config

git clone git@[private-repo]:[user]/[private-rep]
