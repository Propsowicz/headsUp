import React from 'react'

const ChatArea = (props) => {


  return (
    <div>
        <textarea value={props.msg} style={{'width': '350px'}}/>
        {/* <p>{props.msg}</p> */}
    </div>
  )
}

export default ChatArea