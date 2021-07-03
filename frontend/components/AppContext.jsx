import React, { useReducer, createContext } from "react"

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
      case "SET_LOADED": {
        const isLoaded = true
        return {
          ...state,
          isLoaded,
        }
      }
      default:
        return state
    }
  }
  const initialState = {
    auth: {},
    message: {},
    isLoaded: false,
  }
  const [state, dispatch] = useReducer(reducer, initialState)
  const trunkDispatch = getThunkDispatch(dispatch)
  return (
    <AppContext.Provider value={[state, trunkDispatch]}>
      {children}
    </AppContext.Provider>
  )
}
