import logo from './logo.svg';
import './App.css';
import {
  Routes,
  Route,
  BrowserRouter,
  HashRouter
} from 'react-router-dom'
import GameRoom from '../src/pages/GameRoom'
import LoobyRoom from '../src/pages/LoobyRoom'
import HomePage from '../src/pages/HomePage'

function App() {
  return (
    <div>

      <BrowserRouter>
        <Routes>
          <Route path='/' element={<HomePage />}/>
          <Route path='/:game_id/lobby' element={<LoobyRoom />}/>
          <Route path='/:game_id/game' element={<GameRoom />}/>      
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
