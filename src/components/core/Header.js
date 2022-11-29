import React, {useContext} from 'react'
import CreatePlayer from '../home_page/CreatePlayer'
import {UserContext} from '../../context/UserContext'


const Header = () => {
  let {player_id} = useContext(UserContext)

  return (
    <div>
        {player_id ? 
        <></>
        :
        <CreatePlayer />
        }
        
    </div>
  )
}

export default Header