import React, { useState } from "react";
import { Form, Button } from 'react-bootstrap'
import { Link } from "react-router-dom";

const LoginPage = () => {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const LoginUser = () => {
        console.log(username)
        console.log(password)

        setUsername('')
        setPassword('')
    }

    return(
        <div className="container">
            <div className="form">
                <h1>Login</h1>
                <form>
                    <Form.Group>
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Your username"
                                    value={username} name="username" 
                                    onChange={(e)=>{setUsername(e.target.value)}} />
                    </Form.Group>
                    <br></br> 
                    <Form.Group>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Your password"
                                    value={password} name="password"
                                    onChange={(e)=>{setPassword(e.target.value)}}/>
                    </Form.Group>
                    <div className="submit-button">
                        <Form.Group>
                            <Button as="sub" variant="outline-success" onClick={LoginUser}>Login</Button>
                        </Form.Group>
                    </div>
                        <div className="end-notes">
                            <Form.Group>
                                <small> Do not have an account? <Link to='/signup'> SignUp </Link></small>
                            </Form.Group>
                        </div>   
                </form>
            </div>
        </div>
    )
}

export default LoginPage