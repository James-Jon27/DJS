const CREATE = 'stash/create';

//action return
const createStash = (stash) => {
    return {
        type: CREATE,
        payload: stash
    }
}


//thunk create a stash
export const createStashThunk = (stash) => async dispatch => {
    const res = await fetch(`/api/stashes`, {
            method: "POST",
            body: stash
        });

    if(res.ok) {
        const data = await res.json()
        dispatch(createStash(data))
        return data
    } else {
        const err = await res.json()
        return err
    }
}

const initialState = { stash: null }

//switch case 
function stashReducer(state = initialState, action) {
    switch (action.type) {
        case CREATE:
            return {...state, stash: action.payload};
        
        default:
            return state
    }
}

export default stashReducer;
