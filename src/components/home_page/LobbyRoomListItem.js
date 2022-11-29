import React from 'react'
import {Link} from 'react-router-dom'

const LobbyRoomListItem = (props) => {

    function whoIsHost(props){
        for(let i = 0; i < props.players.length; i++){
            if(props.players[i].is_host === true){
                return props.players[i].nickname            
            }
        }
    }

  return (
    <div>
        <Link to={`/${props.id}/lobby/`}>{props.id}, host: {whoIsHost(props)}</Link>    
    </div>
  )
}

export default LobbyRoomListItem