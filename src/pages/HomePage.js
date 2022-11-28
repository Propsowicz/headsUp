import React from 'react'
import {url, ws_url} from '../const/const'
import { w3cwebsocket as W3CWebSocket } from "websocket";


const HomePage = () => {
  const client = new W3CWebSocket(`${ws_url}/ws/home-page/`)

  client.onopen = (data) => {
    console.log('websocket otwarty!!!')
    console.log(data)
  }
  client.onmessage = (message) => {
    let dataFromServer = JSON.parse(message.data)
    console.log(dataFromServer)
    // setMsgs(msgs => [...msgs, dataFromServer])
  }

  return (
    <div>
        <h1>welcome to home-page</h1>

    </div>
  )
}

export default HomePage