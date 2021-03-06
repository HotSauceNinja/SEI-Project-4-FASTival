import React from 'react'
import { useHistory } from 'react-router-dom'
import { loginUser } from '../../lib/api'
import { setToken } from '../../lib/auth'
import useForm from '../../utils/useForm'

function Login(){

  const history = useHistory()
  const [error, setError] = React.useState(false)

  const { formdata, handleChange } = useForm({
    email: '',
    password: ''
  })

  const handleSubmit = async event => {
    event.preventDefault()
    try {      
      const { data } = await loginUser(formdata)
      setToken(data.token)
      history.push('/schedule/')
    } catch (err) {
      setError(true)
    }
  }

  const handleFocus = () => {
    setError(false)
  }

  return (
    <section className="section has-background-dark">
      <div className="container">
        <div className="columns">
          <form className="box column is-half is-offset-one-quarter has-background-dark" onSubmit={handleSubmit}>

            <div className="field">
              <label className="label has-text-info">Email</label>
              <div className="control">
                <input
                  className={`input ${error ? 'is-danger' : ''}`}
                  placeholder="Email"
                  onChange={handleChange}
                  name="email"
                  value={formdata.email}
                  onFocus={handleFocus}
                />
              </div>
            </div>

            <div className="field">
              <label className="label has-text-info">Password</label>
              <div className="control">
                <input
                  type='password'
                  className={`input ${error ? 'is-danger' : ''}`}
                  placeholder="Password"
                  onChange={handleChange}
                  name="password"
                  value={formdata.password}
                />
              </div>
            </div>
            {error && <p className="help is-danger">Your username or password are incorrect</p>}
            <div className="field">
              <button type="submit" className="button is-info has-text-info-light">Login</button>
            </div>

          </form>
        </div>
      </div>
    </section>
  )
}

export default Login