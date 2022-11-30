import React, {useEffect, useState, useContext} from 'react'
import { w3cwebsocket as W3CWebSocket } from "websocket";
import ChatArea from '../components/lobby_room/ChatArea';
import ChatInput from '../components/lobby_room/ChatInput';
import {url, ws_url} from '../const/const'
import {UserContext} from '../context/UserContext'
import {useNavigate} from 'react-router-dom'


const LoobyRoom = () => {
  let room_name = document.location.pathname.split('/')[1]
  let [chatMsg, setChatMsg] = useState('')
  let [host_id, setHost_id] = useState(0)
  let {player_id} = useContext(UserContext)
  const client = new W3CWebSocket(`${ws_url}/ws/${room_name}/lobby/`)

  let navigateGameRoom = useNavigate()

  let getHostId = async () => {
    let response = await fetch(`${url}/game_backend/api/get-host/${room_name}/`)
    let data = await response.json()
    setHost_id(data)
  }

  function checkIfUserIsHost(data){    
    if(data === parseInt(player_id)){
      return true
    }else{
      return false
    }
  }

  let joinGameRoom = async () => {
    let response = await fetch(`${url}/game_backend/api/join-room/${room_name}/`, {
      method: 'POST',
      header: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        'player_id': player_id
      })
    })
  }
  
  let sendMsg = (e) => {
    e.preventDefault()
    client.send(
      JSON.stringify({
        'header': 'MESSAGE',
        'user': player_id,
        'msg': e.target.chat_input.value,
      })
    )
    e.target.chat_input.value = ''
  }

  let startGame = async () => {
    client.send(
      JSON.stringify({
        'header': 'START',
        'user': player_id,
        'msg': 'none',
      })
    )
  }

  
  useEffect(() => {
    getHostId()
    client.onopen = () => {      
        client.send(
        JSON.stringify({
          'header': 'CONNECTED',
          'user': player_id,
          'msg': player_id,
        }))
            
    }

    client.onmessage = (message) => {
      let msg = JSON.parse(message.data)
      console.log(msg)
      if(msg === 'game is starting..'){
        navigateGameRoom(`/${room_name}/game/`)
      }
      setChatMsg(chatMsg = chatMsg + msg + '\n')
    }

  },[])

  return (
    <div>
        <h1>Hello in lobby</h1>
        <ChatArea msg={chatMsg}/>
      
        
        <form onSubmit={sendMsg}>
          <input type='text' name='chat_input'/> <button type='submit'>Wyślij</button>
        </form>
        {checkIfUserIsHost(host_id) 
        ?
        <button onClick={startGame}>Zacznij grę</button>
        : 
        <button onClick={joinGameRoom}>Dołącz do pokoju</button>
        }
        <h2>to do: get list of all players</h2>
        
    </div>
  )
}

export default LoobyRoom