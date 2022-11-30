import React from 'react'

const ChatArea = (props) => {


  return (
    <div>
        <textarea value={props.msg} style={{'width': '550px', 'height': '500px'}}/>
    </div>
  )
}

export default ChatArea