import React from 'react'

const CreateLobbyRoom = (props) => {
    function createNewLobbyRoom(e){props.handleOnClick(e)}

  return (
    <div>
       <button onClick={createNewLobbyRoom}>Stwórz nowy pokój!</button>
    </div>
  )
}

export default CreateLobbyRoom