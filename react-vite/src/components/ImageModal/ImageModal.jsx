export default function ImageModal({id}) {

    return (
        <div className="imgPage">
            <div className="imgUser">
                <div className="img"></div>
                <div className="userInt">
                    <div className="prof"></div>
                    <div className="stashDropdown"></div>
                    <div className="favorite"></div>
                </div>
            </div>
            <span className="imgInfo"></span>
            <span className="comments"></span>
        </div>
    )
}