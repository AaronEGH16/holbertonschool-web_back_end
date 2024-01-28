import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  return Promise
    .all([uploadPhoto(), createUser()])
    .then((values) => console.log(values[0].body, ...Object.values(values[1])))
    .catch(() => console.log('Signup system offline'));
}
