// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://mirusu400.github.io',
  base: '/wipi-wiki',
  trailingSlash: 'ignore',
  integrations: [
    starlight({
      title: 'WIPI Wiki',
      description: 'WIPI 1.2.1 모바일 표준 플랫폼 API 레퍼런스',
      defaultLocale: 'root',
      locales: {
        root: { label: '한국어', lang: 'ko' },
      },
      social: [
        {
          icon: 'github',
          label: 'GitHub',
          href: 'https://github.com/mirusu400/wipi-wiki',
        },
      ],
      editLink: {
        baseUrl: 'https://github.com/mirusu400/wipi-wiki/edit/main/',
      },
      sidebar: [
        {
          label: '개요',
          items: [
            { label: '소개', link: '/overview/' },
            { label: '1. 서론', link: '/overview/introduction/' },
            { label: '2. 개념적 구조', link: '/overview/architecture/' },
            { label: '3. 주요 기능 규격', link: '/overview/platform/' },
          ],
        },
        {
          label: 'HAL 규격',
          items: [
            { label: 'HAL 개요', link: '/hal/' },
            { label: '4.1 Type Definition', link: '/hal/types/' },
            { label: '4.2 플랫폼 API', link: '/hal/platform-api/' },
            { label: '4.3 System', link: '/hal/system/' },
            { label: '4.4 CALL', link: '/hal/call/' },
            { label: '4.5 HandSet Device', link: '/hal/handset/' },
            { label: '4.6 네트워크', link: '/hal/network/' },
            { label: '4.7 Serial', link: '/hal/serial/' },
            { label: '4.8 MEDIA', link: '/hal/media/' },
            { label: '4.9 TIME', link: '/hal/time/' },
            { label: '4.10 UTILITY', link: '/hal/utility/' },
            { label: '4.11 FILE', link: '/hal/file/' },
            { label: '4.12 InputMethod', link: '/hal/input-method/' },
            { label: '4.13 Font', link: '/hal/font/' },
            { label: '4.14 Frame Buffer', link: '/hal/frame-buffer/' },
            { label: '4.15 Virtual Key', link: '/hal/virtual-key/' },
          ],
        },
        {
          label: 'C API',
          items: [
            { label: 'C API 개요', link: '/c-api/' },
            { label: '5.1.1 커널', link: '/c-api/kernel/' },
            { label: '5.1.2 그래픽', link: '/c-api/graphics/' },
            { label: '5.1.3 데이터베이스', link: '/c-api/database/' },
            { label: '5.1.4 파일시스템', link: '/c-api/filesystem/' },
            { label: '5.1.5 NETWORK', link: '/c-api/network/' },
            { label: '5.1.6 매체 처리기', link: '/c-api/media/' },
            { label: '5.1.7 SERIAL', link: '/c-api/serial/' },
            { label: '5.1.8 PHONE', link: '/c-api/phone/' },
            { label: '5.1.9 MISC', link: '/c-api/misc/' },
            { label: '5.1.10 UTILITY', link: '/c-api/utility/' },
            { label: '5.1.11 UI Components', link: '/c-api/ui-components/' },
            { label: '5.1.12 표준 C 라이브러리', link: '/c-api/c-stdlib/' },
          ],
        },
        {
          label: 'Java API',
          collapsed: true,
          items: [{ autogenerate: { directory: 'java-api' } }],
        },
        {
          label: 'CLDC 1.1',
          items: [
            { label: 'CLDC 개요', link: '/cldc/' },
            { label: '규격서', link: '/cldc/spec/' },
            { label: '바이트 코드 검사기', link: '/cldc/verifier/' },
            { label: 'Java API', link: '/cldc/java-api/' },
          ],
        },
        {
          label: 'CLDC Java API',
          collapsed: true,
          items: [{ autogenerate: { directory: 'cldc/java-api' } }],
        },
        {
          label: 'MIDP 2.0',
          items: [
            { label: 'MIDP 개요', link: '/midp/' },
            { label: '개요 문서', link: '/midp/overview/' },
            { label: 'OTA 규격', link: '/midp/ota-spec/' },
            { label: '보안 정책 (GSM/UMTS)', link: '/midp/security-gsm/' },
            { label: '보안 정책 (RP)', link: '/midp/security-rp/' },
            { label: '라이선스', link: '/midp/license/' },
            { label: 'Java API', link: '/midp/java-api/' },
          ],
        },
        {
          label: 'MIDP Java API',
          collapsed: true,
          items: [{ autogenerate: { directory: 'midp/java-api' } }],
        },
        {
          label: '부속서',
          items: [
            { label: '부속서 개요', link: '/appendix/' },
            { label: '6. 참조 문헌', link: '/appendix/references/' },
            { label: '7.1 EUC-KR 확장', link: '/appendix/euc-kr-extended/' },
            { label: '7.2 API 추가/삭제', link: '/appendix/api-management/' },
            { label: '7.3 보안 관련 API', link: '/appendix/security/' },
            { label: '7.4 Media 관련 API', link: '/appendix/media-ext/' },
          ],
        },
      ],
    }),
  ],
});
