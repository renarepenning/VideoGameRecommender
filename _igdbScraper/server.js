/*
install npm request
npm dotenv // to run env file
*/

//https://www.youtube.com/watch?v=-0ASwlMcWik

// init/require packages
require('dotenv').config(); // env is environment variables so we dont have to show client secret
const request = require('request');

// post to twitch to get oauth token
const getToken = (url,callback) => {

    const options = {
        url: process.env.GET_TOKEN,
        json: true,
        body: {
            client_id: process.env.CLIENT_ID,
            client_secret: process.env.CLIENT_SECRET,
            grant_type: 'client_credentials'
            }
    };

    request.post(options, (err, res, body) => {
        if(err){
            return console.log(err);
        }
        console.log("Status: ${res.statusCode");
        console.log(body);

        callback(res);
    });
};


var AT = '';
getToken(process.env.GET_TOKEN,(res) => {
    //console.got(res.body);
    AT = res.body.access_token;
    return AT
})

/* example
setTimeout(() => {
    console.log(AT);
},1000)
*/

// set function to get top games list
const getGames = (url, accessToken, callback) => {

    const gameOptions = {
        url: process.env.GET_GAMES,
        method: 'GET',
        headers:{
            "Client-ID": process.env.CLIENT_ID,
            'Authorization': 'Bearer ' + accessToken
        }
    };
    request.get(gameOptions, (err, res, body) => {
        if(err){
            return console.log(err);
        }
        console.log('Status: ${res.statusCode');
        console.log(JSON.parse(body));
    });

};

setTimeout(() => {
    getGames(process.env.GET_GAMES,AT,(response) =>{

    })
}, 1000)


