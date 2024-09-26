import { createBrowserRouter } from 'react-router-dom';
// import LoginFormPage from '../components/LoginFormPage';
// import SignupFormPage from '../components/SignupFormPage';
import { UserProfileLayout, UserProfilePostedImage, UserProfileStash } from '../components/UserProfilePage'
import HomePage from '../components/HomePage';
import ExplorePage from '../components/ExplorePage/ExplorePage';
import UploadImagePage from '../components/UploadImagePage'
import Layout from './Layout';
import StashPage from '../components/StashPage'
import UploadStash from '../components/UploadStash';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      // {
      //   path: "login",
      //   element: <LoginFormPage />,
      // },
      // {
      //   path: "signup",
      //   element: <SignupFormPage />,
      // },
      {
        path: "explore",
        element: <ExplorePage />
      },
      {
        path: "user/:userId",
        element: <UserProfileLayout />,
        children: [
          {
            path: "posted-images",
            element: <UserProfilePostedImage />
          },
          {
            path: "stashes",
            element: <UserProfileStash />
          }
        ]
      },
      {
        path: "images/new",
        element: <UploadImagePage />
      },
      {
        path: "stashes/new",
        element: <UploadStash />
      }, 
      {
        path: "stashes/:id",
        element: <StashPage />
      }
    ],
  },
]);