import React, {useContext} from 'react'
import {UserContext} from '../../context/UserContext'

const CreatePlayer = () => {
    let {createUser} = useContext(UserContext)

  return (
    <div>
        <h4>Stwórz gracza:</h4>
        <form onSubmit={createUser}>
            <select defaultValue={'female'} name='sex'>
                {/* <option selected>Wybierz płeć</option> */}
                <option value="female">Kobieta</option>
                <option value="male">Mężczyzna</option>            
            </select>
            <button type='submit'>Stwórz gracza</button>
        </form>
    </div>
  )
}

export default CreatePlayer