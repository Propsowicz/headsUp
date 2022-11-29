import React, {useContext, useEffect, useState} from 'react'
import {url, ws_url} from '../const/const'
import { w3cwebsocket as W3CWebSocket } from "websocket";
import CreateLobbyRoom from '../components/home_page/CreateLobbyRoom';
import {UserContext} from '../context/UserContext'
import LobbyRoomListItem from '../components/home_page/LobbyRoomListItem';


const HomePage = () => {
  let {player_id} = useContext(UserContext)
  let [lobby_rooms, set_lobby_rooms] = useState([])
  let [temp_created_lobby, set_temp_created_lobby] = useState([])

  const client = new W3CWebSocket(`${ws_url}/ws/home-page/`)

  client.onopen = () => {
    console.log('websocket otwarty!!!')
  }

  let createNewLobbyRoom = async () => {
    client.send(
      JSON.stringify({
        'header': 'CREATE',
        'host_id': player_id
      })
    )
    set_temp_created_lobby(temp_created_lobby => [...temp_created_lobby, 'new'])
  }  

  useEffect(() => {
    client.onmessage = (message) => {
    let dataFromServer = JSON.parse(message.data)
    set_lobby_rooms(dataFromServer)
    }    
  },[temp_created_lobby])

  return (
    <div>
        <h1>welcome to home-page</h1>
        <CreateLobbyRoom handleOnClick={createNewLobbyRoom}/>
        {lobby_rooms.map((room, index) => (
          <LobbyRoomListItem key={index} id={room.id} is_started={room.is_started} players={room.players}/>
        ))}
        
    </div>
  )
}

export default HomePage