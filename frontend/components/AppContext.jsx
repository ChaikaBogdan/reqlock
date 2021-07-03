import React, { useEffect, useReducer, createContext } from "react"
import { loadAuth } from "../actions.js"

export const AppContext = createContext()

const getThunkDispatch = dispatch => input => input instanceof Function ? input(dispatch) : dispatch(input)

export const AppContextProvider = ({ children }) => {
  const reducer = (state, action) => {
    switch (action.type) {
      case "SET_AUTH": {
        const { payload: auth } = action
        return {
          ...state,
          auth,
        }
      }
      case "SET_MESSAGE": {
        const { payload: message } = action
        return {
          ...state,
          message,
        }
      }
      default:
        return state
    }
  }
  const initialState = {
    auth: {},
    message: {},
  }
  const [state, dispatch] = useReducer(reducer, initialState)
  const trunkDispatch = getThunkDispatch(dispatch)

  useEffect(() => {
    trunkDispatch(loadAuth)
  }, [])
  return (
    <AppContext.Provider value={[state, trunkDispatch]}>
      {children}
    </AppContext.Provider>
  )
}
