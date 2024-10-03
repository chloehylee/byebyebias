// import { useState } from 'react'
import './App.css'
import axios from 'axios'
import React from 'react'

class App extends React.Component {
  state = {details: [],  }
  
  componentDidMount(): void {
    let data;
    axios.get('http://127.0.0.1:8000/')
    .then(res => {
      data = res.data;
      this.setState({
        details: data
      })
    })
    .catch(err => {})
  }

  render() {
    return (
      <div>
        <header>Data Generated From Django</header>
        <hr></hr>
        {this.state.details.map((output, id) => (
          <div key={id}>
            <h2>{output.employee}</h2>
            <h3>{output.department}</h3>
          </div>
        ))}
      </div>
    )
  }

}

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <h1>Triple B</h1>
//       <h2>Bye Bye Bias!</h2>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
        
//       </div>

//     </>
//   )
// }

export default App
