import React, {useState} from "react"
import { Form, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { useForm } from 'react-hook-form'

const SignUpPage = () => {

    const {register, watch, handleSubmit, reset, formState: { errors }} = useForm();

    const SubmitForm = (data) => {

        if (data.password === data.confirmPassword) {
            
            const body = {
                username: data.username,
                email: data.email,
                password: data.password
            }

            const requestOptions = {
                method: "POST",
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify(body)
            }
            
            fetch('http://localhost:5000/auth/signup', requestOptions)
            .then((res) => {
                if (!res.ok) {
                  throw new Error('Request failed');
                }
                return res.json();
              })
            .then(data => console.log(data))
            .catch(err => console.log(err))
            reset()
        }

        else {
            alert("Passwords do not match")
        }
       
    }

    return(
        <div className="container">
            <div className="form">
                <h1>SignUp</h1>
                <form>
                    <Form.Group>
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Your username"
                                      {...register("username", {required:true, maxLength:25})} />
                    {errors.username?.type === "required" && <p style={{color:"red"}}><small>Username is required</small></p>}
                    {errors.username?.type === "maxLength" && (<p style={{ color: "red" }}>Username is too long</p>)}
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Email</Form.Label>
                        <Form.Control type="email" placeholder="Your email"
                                      {...register("email", {required:true, maxLength:80})} />
                    {errors.email?.type === "required" && <p style={{color:"red"}}><small>Email is required</small></p>}
                    {errors.email?.type === "maxLength" && <p style={{color:"red"}}><small>Email is too long</small></p>}
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Your password"
                                      {...register("password", {required:true, minLength:8})} />
                    {errors.password?.type === "required" && <p style={{color:"red"}}><small>Password is required</small></p>}
                    {errors.password?.type === "minLength" && <p style={{color:"red"}}><small>Password must contain at least 8 characters</small></p>}
                    </Form.Group>
                    <Form.Group>
                        <Form.Label>Confirm Password</Form.Label>
                        <Form.Control type="password" placeholder="Your password"
                                      {...register("confirmPassword", {required:true, minLength:8})}/>
                    {errors.confirmPassword?.type === "required" && <p style={{color:"red"}}><small>Password is required</small></p>}
                    {errors.confirmPassword?.type === "minLength" && <p style={{color:"red"}}><small>Password must contain at least 8 characters</small></p>}
                    </Form.Group>
                    <div className="submit-button">
                        <Form.Group>
                            <Button as="sub" variant="outline-success" onClick={handleSubmit(SubmitForm)}>SignUp</Button>
                        </Form.Group>
                    </div>
                    <div className="end-notes">
                        <Form.Group>
                            <small> Already have an account? <Link to='/login'> Login </Link></small>
                        </Form.Group>      
                    </div>
                </form>
            </div>
        </div>
    )
}

export default SignUpPage