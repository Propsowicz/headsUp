import React, {useEffect, useState} from 'react'
import { w3cwebsocket as W3CWebSocket } from "websocket";
import ChatArea from '../components/lobby_room/ChatArea';
import ChatInput from '../components/lobby_room/ChatInput';
import {url, ws_url} from '../const/const'


const LoobyRoom = () => {
  let rooma_name = document.location.pathname.split('/')[1]
  let [chatMsg, setChatMsg] = useState([])
  let [isPlayerConnected, setPlayerConnection] = useState(false)
  const client = new W3CWebSocket(`${ws_url}/ws/${rooma_name}/lobby/`)

  client.onopen = () => {
    console.log('połączono')
    if(!isPlayerConnected){
      setPlayerConnection(!isPlayerConnected)
      client.send(
      JSON.stringify({
        'header': 'CONNECTED',
        'user': localStorage.getItem('player_id'),
        'msg': localStorage.getItem('player_id'),
      }))
      }     
  }

  let sendMsg = (e) => {
    e.preventDefault()
    client.send(
      JSON.stringify({
        'header': 'MESSAGE',
        'user': localStorage.getItem('player_id'),
        'msg': e.target.chat_input.value,
      })
    )
    e.target.chat_input.value = ''
  }



  
  useEffect(() => {
    client.onmessage = (message) => {
      let msg = JSON.parse(message.data)
      setChatMsg(chatMsg => [...chatMsg, msg])
    }

  },[])

  return (
    <div>
        <h1>Hello in lobby</h1>
        {chatMsg.map((new_msg, index) => (
          <ChatArea msg={new_msg} key={index}/>
        ))}
        
        <form onSubmit={sendMsg}>
          <input type='text' name='chat_input'/> <button type='submit'>Wyślij</button>
        </form>
        
    </div>
  )
}

export default LoobyRoom