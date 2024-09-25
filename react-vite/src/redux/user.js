const GET_USER_BY_ID = 'user/getUserById'

const getUserById = (user) => ({
    type: GET_USER_BY_ID,
    payload: user
})

export const thunkGetUserById = userId => async dispatch => {
    const response = await fetch(`/api/users/${userId}`);
    if (response.ok) {
        const user = await response.json();
        if (user.errors) {
            return;
        }

        dispatch(getUserById(user))
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