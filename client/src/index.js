import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/main.css'
import React, {Fragment} from 'react'
import ReactDOM from 'react-dom'
import NavBar from './components/Navbar';

import {
    BrowserRouter as Router,
    Routes,
    Route
} from 'react-router-dom'

import HomePage from './components/Home';
import SignUpPage from './components/Signup';
import CreatePlaylistPage from './components/CreatePlaylist';
import LoginPage from './components/Login';

const App = () => {

    return (
        <Router>
            <Fragment>
            <div className="">
                <NavBar/>
                <Routes>
                    <Route exact path="/create_recipe" element={<CreatePlaylistPage/>}>     
                    </Route>                
                    <Route exact path="/login" element={<LoginPage/>}>
                    </Route>
                    <Route exact path="/signup" element={<SignUpPage/>}>
                    </Route>
                    <Route exact path="/" element={<HomePage/>}>
                    </Route>
                </Routes>
            </div>
            </Fragment>
        </Router>
    )
}

ReactDOM.render(<App/>, document.getElementById('root'));