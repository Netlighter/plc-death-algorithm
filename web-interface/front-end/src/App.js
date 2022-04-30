import logo from './logo.svg';
import './App.css';
import { Button } from 'antd';
import Header from './components/Header/Header'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Header></Header>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <Button type="primary">FUCK!</Button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
