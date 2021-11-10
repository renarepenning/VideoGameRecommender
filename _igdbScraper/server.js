/*
install npm request
npm dotenv // to run env file
*/

//https://www.youtube.com/watch?v=-0ASwlMcWik

// init/require packages
require('dotenv').config(); // env is environment variables so we dont have to show client secret
const request = require('request');

// must install axios with npm
// axios.<method> will now provide autocomplete and parameter typings
const axios = require('axios').default;

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


axios({
    url: "https://api.igdb.com/v4/companies",
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Client-ID': process.env.CLIENT_ID,
        'Authorization': 'Bearer ' + getToken

    },
    data: "fields change_date,change_date_category,changed_company_id,checksum,country,created_at,description,developed,logo,name,parent,published,slug,start_date,start_date_category,updated_at,url,websites;"
  })
    .then(response => {
        console.log(response.data);
    })
    .catch(err => {
        console.error(err);
    });



// setTimeout(() => {
//     getGames(process.env.GET_GAMES,AT,(response) =>{
    
//     })
// }, 1000)







/* example
setTimeout(() => {
    console.log(AT);
},1000)


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

*/

