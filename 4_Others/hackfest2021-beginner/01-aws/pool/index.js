const AWS = require("aws-sdk");

const credentials = new AWS.CognitoIdentityCredentials({
   IdentityPoolId: "us-east-1:153b276b-5ce9-4ec2-a556-f1919eeacd2e" // e.g., us-east-1:d40a3a95-a6b5-4816-a15c-a15ac4f0930d
});

const client = new AWS.Location({
   credentials,
   region: AWS.config.region || "us-east-1"
});

const run = async () => {
    try {
            const valeur = await client.listMaps().promise();
            console.log(valeur);
        } catch (err) {
            console.error(err);
        }
    };
run();