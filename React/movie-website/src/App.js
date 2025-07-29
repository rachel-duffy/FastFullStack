import React, {useState, useEffect} from 'react'
import axios from "axios";
import './App.css';

function App() {
  const [movieData, setMovieData] = useState([]);

  useEffect(() => {
      const fetchData = async () => {
          const response = await axios.get('http://127.0.0.1:8000/movie');
          setMovieData(response.data);
      }
      fetchData();
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <h1>My Movies</h1>
        <ul>
            { movieData.map((movie, index) => {
                return <li key={index}>{movie.name}</li>;
            })}
        </ul>
      </header>
    </div>
  );
}

export default App;
