#!/usr/bin/node 
// made by prince kumar 
// date 20 march 2022
const TelegramBot = require('node-telegram-bot-api');
require('dotenv').config()
const token = process.env.API_KEY;
const bot = new TelegramBot(token, {polling: true});
bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    let uname = msg.sender_chat.title;
    if (msg.text == "hi" | msg.text == "hii"){
        bot.sendMessage(chatId,`hello ${uname}`);

    }
    else if (msg.text == "good morning" | msg.text == "good_morning"){
        bot.sendMessage(chatId,`Good Morning ${uname}`);

    }
    else {
        console.log("hi");
    }
    // send a message to the chat acknowledging receipt of their message
  
    
  });

  bot.sendMessage(chatId,`${name} sent ${msg.text}`);