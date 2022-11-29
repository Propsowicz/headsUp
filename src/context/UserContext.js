import React, {createContext, useEffect, useState} from 'react'
import {url} from '../const/const'

export const UserContext = createContext()


export const UserContextProvider = ({children}) => {
    let [player_id, set_player_id] = useState(localStorage.getItem('player_id') ? localStorage.getItem('player_id'): [])

    let createUser = async (e) => {
        e.preventDefault()
        let response = await fetch(`${url}/player/api/create/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                'sex': e.target.sex.value
            })
        })
        let data = await response.json()
        localStorage.setItem('player_id', data.id)
        set_player_id(data.id)
    }

    useEffect(() => {
        console.log(player_id)        
    }, [player_id])

    let contextData = {
        createUser: createUser,

        player_id: player_id
    }


    return (
        <UserContext.Provider value={contextData}>
            {children}
        </UserContext.Provider>
      )
    
}
   


