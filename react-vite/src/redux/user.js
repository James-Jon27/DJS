// actions
const GET_USER_BY_ID = 'user/getUserById'
const GET_STASH_FROM_USER = 'user/getStashFromUser'

// action creators
const getUserById = (user) => {
    return {
        type: GET_USER_BY_ID,
        payload: user
    }
}


// thunks
export const thunkGetUserById = userId => async dispatch => {
    const response = await fetch(`/api/users/${userId}`);
    if (response.ok) {
        const user = await response.json();
        if (user.errors) {
            return;
        }

        dispatch(getUserById(user))
    }
    else {
        const err = await response.json()
        return err
    }
}

function userReducer(state = {}, action) {
    switch (action.type) {
        case GET_USER_BY_ID:
            return action.payload
        default:
            return state
    }
}

export default userReducer;