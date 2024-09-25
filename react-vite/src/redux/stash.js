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
    const res = await fetch("/api/stashes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(stash)
        });

    if(res.ok) {
        const data = await res.json()
        dispatch(createStash(data))
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
    }
}

export default stashReducer;
