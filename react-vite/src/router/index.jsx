import { createBrowserRouter } from 'react-router-dom';
// import LoginFormPage from '../components/LoginFormPage';
// import SignupFormPage from '../components/SignupFormPage';
import { UserProfileLayout, UserProfilePostedImage, UserProfileStash } from '../components/UserProfilePage'
import HomePage from '../components/HomePage';
import UploadImagePage from '../components/UploadImagePage'
import Layout from './Layout';
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
        path: "user",
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
      }
      
    ],
  },
]);