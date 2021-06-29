import { Components } from 'antd/lib/date-picker/generatePicker';
import React ,{Component} from 'react'
import classes from './newlogin.css'
class Login extends Component{

    state = {

        style : classes["container"]
    }
    componentDidMount(){

    }

    




    render(){

        const onSignInClick = ()=>{
            console.log('Hi')
            this.setState({
                style:classes["container"]
            })

        }

        const onSignUpClick = ()=>{

            this.setState({
                style:[classes["container"],classes["right-panel-active"]].join(' ')
            })
        }

        const onForgetClick = ()=>{
        
            this.setState({
                style:[classes["container"],classes["left-panel-active"]].join(' ')
            })
        }

        return (
           
        
        <div className={this.state.style} id="container">
                <div className={[classes["form-container"], classes["sign-up-container"]].join(' ')}>
                    <form action="#">
                        <h1>Create Account</h1>
                        <div className={classes["social-container"]}>
                            <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
                            <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
                            <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
                        </div>
                        <span>or use your email for registration</span>
                        <input type="text" placeholder="Name" />
                        <input type="email" placeholder="Email" />
                        <input type="password" placeholder="Password" />
                        <button >Sign Up</button>
                    </form>
                </div>
                <div className={[classes["form-container"],classes["sign-in-container"]].join(' ')}>
                    <form action="#">
                        <h1>Sign in</h1>
                        <div className={classes["social-container"]}>
                            <a href="#" className={classes["social"]}><i class="fab fa-facebook-f"></i></a>
                            <a href="#" className={classes["social"]}><i class="fab fa-google-plus-g"></i></a>
                            <a href="#" className={classes["social"]}><i class="fab fa-linkedin-in"></i></a>
                        </div>
                        <span>or use your account</span>
                        <input type="email" placeholder="Email" />
                        <input type="password" placeholder="Password" />
                        <a href="#" onClick={onForgetClick}>Forgot your password?</a>
                        <button >Sign In</button>
                    </form>
                </div>

                <div className={[classes["form-container"],classes["forget-container"]].join(' ')}>
                    <form action="#">
                        <h1>Forget</h1>
                        <input type="email" placeholder="Email" />
                        <input type="password" placeholder="Password" />
                        <button >Forget</button>
                    </form>
                </div>
           
                <div className={classes["overlay-container"]}>
                    <div className={classes["overlay"]}>
                        <div className={[classes["overlay-panel"],classes["overlay-left"]].join(' ')}>
                            <h1>Welcome Back!</h1>
                            <p>To keep connected with us please login with your personal info</p>
                            <button onClick={onSignInClick} class="ghost" id="signIn">Sign In</button>
                        </div>
                        <div className={[classes["overlay-panel"],classes["overlay-right"]].join(' ')}>
                            <h1>Hello, Friend!</h1>
                            <p>Enter your personal details and start journey with us</p>
                            <button className={classes["ghost"]}   onClick={onSignUpClick} id="signUp">Sign Up</button>
                        </div>
                    </div>
                </div>

                
            </div>
        
        
        )
    }
}

export default Login;